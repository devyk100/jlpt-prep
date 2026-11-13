import React, { useState, useEffect } from 'react';
import { History, X, Search, Star, Trash2, Copy, Check } from 'lucide-react';
import { HistoryEntry } from '../types';

interface HistoryModalProps {
  onClose: () => void;
}

export const HistoryModal: React.FC<HistoryModalProps> = ({ onClose }) => {
  const [entries, setEntries] = useState<HistoryEntry[]>([]);
  const [search, setSearch] = useState('');
  const [isLoading, setIsLoading] = useState(true);
  const [copiedId, setCopiedId] = useState<number | null>(null);

  const fetchHistory = async () => {
    if (!window.pywebview?.api) return;
    setIsLoading(true);
    try {
      const data = await window.pywebview.api.get_history(50, 0, search);
      setEntries(data);
    } catch (e) {
      console.error('Fetch history error:', e);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchHistory();
  }, [search]);

  const handleToggleFavorite = async (id: number) => {
    if (!window.pywebview?.api) return;
    try {
      const isFav = await window.pywebview.api.toggle_favorite(id);
      setEntries((prev) =>
        prev.map((e) => (e.id === id ? { ...e, is_favorite: isFav } : e))
      );
    } catch (e) {
      console.error('Toggle favorite error:', e);
    }
  };

  const handleDelete = async (id: number) => {
    if (!window.pywebview?.api) return;
    try {
      await window.pywebview.api.delete_history_entry(id);
      setEntries((prev) => prev.filter((e) => e.id !== id));
    } catch (e) {
      console.error('Delete error:', e);
    }
  };

  const handleCopy = (id: number, text: string) => {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 1500);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-md p-4">
      <div className="w-full max-w-xl bg-neutral-900 border border-white/10 rounded-xl shadow-2xl overflow-hidden flex flex-col text-neutral-200 h-[80vh]">
        {/* Header */}
        <div className="flex items-center justify-between px-4 py-2.5 border-b border-white/10 bg-neutral-800/50">
          <div className="flex items-center gap-2 text-rose-400 font-semibold text-sm">
            <History className="w-4 h-4" />
            <span>Reading & Dialogue History</span>
          </div>
          <button onClick={onClose} className="p-1 hover:text-white rounded hover:bg-white/10">
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Search */}
        <div className="p-3 border-b border-white/5 bg-neutral-800/20 flex items-center gap-2">
          <div className="relative flex-1">
            <Search className="w-3.5 h-3.5 absolute left-2.5 top-1/2 -translate-y-1/2 text-neutral-500" />
            <input
              type="text"
              placeholder="Search Japanese word, sentence, or meaning..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="w-full bg-neutral-800 border border-white/10 rounded-lg pl-8 pr-3 py-1.5 text-xs text-white focus:outline-none focus:border-rose-500"
            />
          </div>
        </div>

        {/* List */}
        <div className="flex-1 overflow-y-auto p-3 flex flex-col gap-2.5">
          {isLoading ? (
            <div className="text-center py-10 text-neutral-500 text-xs">Loading history...</div>
          ) : entries.length === 0 ? (
            <div className="text-center py-12 text-neutral-500 text-xs">
              No saved entries found. Press <span className="text-rose-400 font-mono">F8</span> during a game to capture.
            </div>
          ) : (
            entries.map((item) => (
              <div
                key={item.id}
                className="p-3 rounded-lg bg-white/5 border border-white/5 hover:border-white/10 transition flex flex-col gap-1.5"
              >
                <div className="flex items-start justify-between gap-2">
                  <div className="flex flex-col gap-0.5">
                    <p className="text-sm font-japanese font-medium text-white">{item.japanese}</p>
                    {item.translation && (
                      <p className="text-xs text-neutral-300 italic">"{item.translation}"</p>
                    )}
                  </div>

                  <div className="flex items-center gap-1 shrink-0">
                    <button
                      onClick={() => handleToggleFavorite(item.id)}
                      title="Star favourite"
                      className={`p-1 rounded transition ${
                        item.is_favorite
                          ? 'text-amber-400 hover:text-amber-300'
                          : 'text-neutral-500 hover:text-white'
                      }`}
                    >
                      <Star className={`w-3.5 h-3.5 ${item.is_favorite ? 'fill-amber-400' : ''}`} />
                    </button>

                    <button
                      onClick={() => handleCopy(item.id, item.japanese)}
                      title="Copy sentence"
                      className="p-1 text-neutral-400 hover:text-white rounded"
                    >
                      {copiedId === item.id ? (
                        <Check className="w-3.5 h-3.5 text-emerald-400" />
                      ) : (
                        <Copy className="w-3.5 h-3.5" />
                      )}
                    </button>

                    <button
                      onClick={() => handleDelete(item.id)}
                      title="Delete entry"
                      className="p-1 text-neutral-500 hover:text-rose-400 rounded"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>
                </div>

                <div className="flex items-center justify-between text-[10px] text-neutral-500 border-t border-white/5 pt-1 mt-1">
                  <span>{item.source}</span>
                  <span>{item.timestamp}</span>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};
