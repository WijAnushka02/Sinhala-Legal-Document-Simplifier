/**
 * Shared TypeScript interfaces for the Sinhala Legal Document Simplifier.
 */

export type Language = 'si' | 'ta' | 'en';

export type LegalCategory =
  | 'consumer_law'
  | 'labour_law'
  | 'property_law'
  | 'family_law'
  | 'criminal_law'
  | 'administrative_law'
  | 'general';

export type SessionStatus = 'pending' | 'processing' | 'done' | 'error';

export interface User {
  id: string;
  email: string;
  display_name: string | null;
  preferred_lang: Language;
  created_at: string;
}

export interface ExtractedEntity {
  text: string;
  type: string;
}

export interface SourceReference {
  source_id: string;
  title: string;
  section?: string;
  relevance_score: number;
  url?: string;
}

export interface SimplifyResponse {
  session_id: string;
  status: SessionStatus;
  original_text?: string;
  simplified_text?: string;
  clause_types: string[];
  entities: ExtractedEntity[];
  conditions: string[];
  obligations: string[];
  exceptions: string[];
  dates: Record<string, unknown>[];
  numbers: Record<string, unknown>[];
  meaning_score?: number;
  sources: SourceReference[];
  processing_time_ms?: number;
  slm_used: boolean;
  rag_used: boolean;
  gemini_used: boolean;
  error_message?: string;
  created_at?: string;
}

export interface SimplifyRequest {
  input_type: 'text' | 'document';
  text?: string;
  document_id?: string;
  language: Language;
  legal_category?: LegalCategory;
  question?: string;
  use_rag: boolean;
  use_gemini: boolean;
}

export interface QueryResponse {
  session_id: string;
  answer: string;
  sources: SourceReference[];
  confidence?: number;
  processing_time_ms?: number;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
  expires_in: number;
}

export interface ApiError {
  detail: string;
  status: number;
}
