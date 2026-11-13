# YomiFlow Windows Native Japanese OCR Worker Bridge
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]

function AwaitTask($WinRtTask, $ResultType) {
    $netTask = $asTaskGeneric.MakeGenericMethod($ResultType).Invoke($null, @($WinRtTask))
    $netTask.Wait(-1) | Out-Null
    $netTask.Result
}

[Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType = WindowsRuntime] | Out-Null
[Windows.Media.Ocr.OcrEngine, Windows.Media.Ocr, ContentType = WindowsRuntime] | Out-Null
[Windows.Globalization.Language, Windows.Globalization, ContentType = WindowsRuntime] | Out-Null

$lang = [Windows.Globalization.Language]::new("ja")
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($lang)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::WriteLine("READY")

while ($line = [Console]::ReadLine()) {
    if ($line -eq "EXIT") { break }
    if ([string]::IsNullOrWhiteSpace($line)) { continue }
    try {
        $file = AwaitTask ([Windows.Storage.StorageFile]::GetFileFromPathAsync($line)) ([Windows.Storage.StorageFile])
        $stream = AwaitTask ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
        $decoder = AwaitTask ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
        $bitmap = AwaitTask ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
        $ocr = AwaitTask ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
        $stream.Dispose()
        
        $lines = @()
        foreach ($l in $ocr.Lines) {
            # Strip inter-glyph spaces inserted by CJK tokenizer while preserving line structure
            $cleanedLine = $l.Text -replace '\s+', ''
            if (![string]::IsNullOrWhiteSpace($cleanedLine)) {
                $lines += $cleanedLine
            }
        }
        
        $fullText = $lines -join "`n"
        
        $outObj = @{
            text = $fullText
            lines = $lines
            count = $lines.Count
        }
        $json = ConvertTo-Json -Compress $outObj
        [Console]::WriteLine($json)
    } catch {
        $errObj = @{ error = $_.Exception.Message }
        $errJson = ConvertTo-Json -Compress $errObj
        [Console]::WriteLine($errJson)
    }
}
