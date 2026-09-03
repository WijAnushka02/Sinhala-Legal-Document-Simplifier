import { useState, useCallback } from 'react';
import apiClient from '../api/client';
import type { Language, LegalCategory, SimplifyResponse } from '../types';

const LEGAL_CATEGORIES: { value: LegalCategory; label: string; si: string }[] = [
  { value: 'consumer_law', label: 'Consumer Law', si: 'පාරිභෝගික නීතිය' },
  { value: 'labour_law', label: 'Labour Law', si: 'කම්කරු නීතිය' },
  { value: 'property_law', label: 'Property Law', si: 'දේපළ නීතිය' },
  { value: 'family_law', label: 'Family Law', si: 'පවුල් නීතිය' },
  { value: 'general', label: 'General', si: 'සාමාන්‍ය' },
];

const CLAUSE_BADGE_CLASS: Record<string, string> = {
  OBLIGATION: 'badge badge-obligation',
  RIGHT: 'badge badge-right',
  CONDITION: 'badge badge-condition',
  DEADLINE: 'badge badge-deadline',
};

export default function HomePage() {
  const [language, setLanguage] = useState<Language>('si');
  const [category, setCategory] = useState<LegalCategory>('consumer_law');
  const [text, setText] = useState('');
  const [result, setResult] = useState<SimplifyResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const pollResult = useCallback(async (sessionId: string) => {
    const maxAttempts = 30;
    for (let i = 0; i < maxAttempts; i++) {
      await new Promise((r) => setTimeout(r, 2000));
      const { data } = await apiClient.get<SimplifyResponse>(`/simplify/${sessionId}`);
      if (data.status === 'done' || data.status === 'error') {
        return data;
      }
    }
    throw new Error('Processing timeout');
  }, []);

  const handleSimplify = async () => {
    if (!text.trim()) return;
    setIsLoading(true);
    setError(null);
    setResult(null);

    try {
      const { data } = await apiClient.post<SimplifyResponse>('/simplify', {
        input_type: 'text',
        text,
        language,
        legal_category: category,
        use_rag: true,
        use_gemini: true,
      });

      const final = await pollResult(data.session_id);
      setResult(final);
    } catch (err: any) {
      setError(err?.response?.data?.detail || 'An error occurred. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      {/* Navbar */}
      <nav className="navbar">
        <div className="container navbar-inner">
          <a href="/" className="navbar-brand">
            🇱🇰 Sinhala Legal Simplifier
          </a>
          <span className="text-muted" style={{ fontSize: '0.85rem' }}>
            AI-Powered Legal Understanding
          </span>
        </div>
      </nav>

      <main className="container" style={{ padding: '2rem 1.5rem 4rem' }}>

        {/* Hero */}
        <div style={{ textAlign: 'center', marginBottom: '2.5rem' }}>
          <h1 style={{ fontSize: '2rem', fontWeight: 700, lineHeight: 1.3, marginBottom: '0.75rem' }}>
            නීතිමය ලේඛන සරලව තේරුම් ගන්න
          </h1>
          <p className="text-muted" style={{ fontSize: '1.05rem', maxWidth: '560px', margin: '0 auto' }}>
            Upload or paste Sri Lankan legal text and get a simplified explanation
            that preserves the original legal meaning.
          </p>
        </div>

        {/* Input card */}
        <div className="card" style={{ marginBottom: '1.5rem' }}>

          {/* Language selector */}
          <div className="mb-2">
            <label className="label">Language / භාෂාව</label>
            <div className="lang-selector">
              {(['si', 'ta', 'en'] as Language[]).map((lang) => (
                <button
                  key={lang}
                  className={`lang-btn ${language === lang ? 'active' : ''}`}
                  onClick={() => setLanguage(lang)}
                >
                  {lang === 'si' ? 'සිංහල' : lang === 'ta' ? 'தமிழ்' : 'English'}
                </button>
              ))}
            </div>
          </div>

          {/* Category */}
          <div className="mb-2">
            <label className="label">Legal Category / නීතිමය ප්‍රවර්ගය</label>
            <select
              className="select"
              value={category}
              onChange={(e) => setCategory(e.target.value as LegalCategory)}
            >
              {LEGAL_CATEGORIES.map((c) => (
                <option key={c.value} value={c.value}>
                  {c.si} — {c.label}
                </option>
              ))}
            </select>
          </div>

          {/* Text input */}
          <div className="mb-2">
            <label className="label">Legal Text / නීතිමය පාඨය</label>
            <textarea
              className="textarea si"
              placeholder="නීතිමය පාඨය මෙහි ඇතුළු කරන්න... / Paste legal text here..."
              value={text}
              onChange={(e) => setText(e.target.value)}
              rows={6}
            />
          </div>

          {error && (
            <p className="text-error mt-1" style={{ fontSize: '0.9rem' }}>⚠ {error}</p>
          )}

          <button
            className="btn btn-primary mt-2"
            onClick={handleSimplify}
            disabled={isLoading || !text.trim()}
            style={{ width: '100%', justifyContent: 'center', fontSize: '1rem', padding: '0.8rem' }}
          >
            {isLoading ? (
              <>
                <span className="spinner" style={{ width: 18, height: 18, borderWidth: 2 }} />
                සරල කරමින්…
              </>
            ) : (
              '✨ Simplify / සරල කරන්න'
            )}
          </button>
        </div>

        {/* Result */}
        {result && result.status === 'done' && (
          <div className="card">
            <h2 style={{ fontSize: '1.1rem', fontWeight: 600, marginBottom: '1rem' }}>
              📋 Result / ප්‍රතිඵලය
            </h2>

            <div className="result-grid">
              <div>
                <p className="label">Original / මුල් පාඨය</p>
                <div className="result-box si">{result.original_text}</div>
              </div>
              <div>
                <p className="label text-success">Simplified / සරල කළ පාඨය</p>
                <div className="result-box simplified si">{result.simplified_text}</div>
              </div>
            </div>

            {/* Clause types */}
            {result.clause_types.length > 0 && (
              <div className="mt-2 flex gap-2" style={{ flexWrap: 'wrap' }}>
                {result.clause_types.map((ct) => (
                  <span key={ct} className={CLAUSE_BADGE_CLASS[ct] || 'badge'}>
                    {ct}
                  </span>
                ))}
              </div>
            )}

            {/* Meaning score */}
            {result.meaning_score != null && (
              <div className="mt-2">
                <p className="label">
                  Meaning Preserved / අර්ථ සංරක්ෂණය — {Math.round(result.meaning_score * 100)}%
                </p>
                <div className="meaning-bar">
                  <div className="meaning-fill" style={{ width: `${result.meaning_score * 100}%` }} />
                </div>
              </div>
            )}

            {/* Sources */}
            {result.sources.length > 0 && (
              <div className="mt-3">
                <p className="label">Sources / මූලාශ්‍ර</p>
                {result.sources.map((src) => (
                  <div key={src.source_id} className="card mt-1" style={{ padding: '0.75rem' }}>
                    <p style={{ fontWeight: 600, fontSize: '0.9rem' }}>{src.title}</p>
                    {src.section && <p className="text-muted" style={{ fontSize: '0.82rem' }}>{src.section}</p>}
                    <p className="text-muted" style={{ fontSize: '0.8rem' }}>
                      Relevance: {Math.round(src.relevance_score * 100)}%
                    </p>
                  </div>
                ))}
              </div>
            )}

            {/* Pipeline info */}
            <p className="text-muted mt-2" style={{ fontSize: '0.8rem' }}>
              {result.slm_used && '🤖 SLM '}{result.rag_used && '📚 RAG '}{result.gemini_used && '✨ Gemini '}
              {result.processing_time_ms && `· ${result.processing_time_ms}ms`}
            </p>

            {/* Legal disclaimer */}
            <div style={{
              marginTop: '1.5rem', padding: '0.75rem 1rem',
              background: 'rgba(251,191,36,0.08)', borderRadius: 'var(--radius-md)',
              border: '1px solid rgba(251,191,36,0.2)',
            }}>
              <p className="si" style={{ fontSize: '0.82rem', color: 'var(--color-warning)' }}>
                ⚠ මෙම පද්ධතිය නීතිමය උපදෙස් ලබා දීම සඳහා නොවේ. නීතිමය තීරණ ගැනීමට පෙර නිල
                මූලාශ්‍ර හෝ නීතිමය වෘත්තිකයෙකුගෙන් උපදෙස් ලබා ගන්න.
              </p>
            </div>
          </div>
        )}

        {result?.status === 'error' && (
          <div className="card">
            <p className="text-error">Processing failed: {result.error_message}</p>
          </div>
        )}
      </main>
    </>
  );
}
