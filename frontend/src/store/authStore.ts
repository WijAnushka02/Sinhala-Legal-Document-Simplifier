import { create } from 'zustand';
import type { User } from '../types';
import { setAccessToken } from '../api/client';
import apiClient from '../api/client';

interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  checkAuth: () => Promise<void>;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  isAuthenticated: false,
  isLoading: true,

  login: async (email: string, password: string) => {
    const { data } = await apiClient.post('/auth/login', { email, password });
    setAccessToken(data.access_token);
    const { data: user } = await apiClient.get<User>('/auth/me');
    set({ user, isAuthenticated: true });
  },

  logout: async () => {
    try { await apiClient.post('/auth/logout'); } catch { /* ignore */ }
    setAccessToken(null);
    set({ user: null, isAuthenticated: false });
    window.location.href = '/login';
  },

  checkAuth: async () => {
    try {
      // Attempt silent refresh using HttpOnly cookie
      const { data } = await apiClient.post('/auth/refresh');
      setAccessToken(data.access_token);
      const { data: user } = await apiClient.get<User>('/auth/me');
      set({ user, isAuthenticated: true, isLoading: false });
    } catch {
      set({ user: null, isAuthenticated: false, isLoading: false });
    }
  },
}));
