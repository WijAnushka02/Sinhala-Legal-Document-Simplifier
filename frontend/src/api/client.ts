/**
 * Axios API client with JWT interceptor.
 * Access token stored in-memory (not localStorage) for security.
 * Refresh token is an HttpOnly cookie (handled by browser automatically).
 */
import axios, { type AxiosInstance, type InternalAxiosRequestConfig } from 'axios';

// In-memory token store (not accessible to XSS)
let accessToken: string | null = null;

export const setAccessToken = (token: string | null) => { accessToken = token; };
export const getAccessToken = () => accessToken;

const apiClient: AxiosInstance = axios.create({
  baseURL: '/api/v1',
  withCredentials: true,  // Send HttpOnly cookies (refresh token)
  headers: { 'Content-Type': 'application/json' },
});

// Request interceptor — attach access token
apiClient.interceptors.request.use((config: InternalAxiosRequestConfig) => {
  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }
  return config;
});

// Response interceptor — auto-refresh on 401
let isRefreshing = false;
let refreshQueue: Array<(token: string) => void> = [];

apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      if (isRefreshing) {
        // Queue requests while refreshing
        return new Promise((resolve) => {
          refreshQueue.push((token) => {
            originalRequest.headers.Authorization = `Bearer ${token}`;
            resolve(apiClient(originalRequest));
          });
        });
      }

      originalRequest._retry = true;
      isRefreshing = true;

      try {
        const { data } = await apiClient.post<{ access_token: string }>('/auth/refresh');
        setAccessToken(data.access_token);
        refreshQueue.forEach((cb) => cb(data.access_token));
        refreshQueue = [];
        originalRequest.headers.Authorization = `Bearer ${data.access_token}`;
        return apiClient(originalRequest);
      } catch {
        setAccessToken(null);
        window.location.href = '/login';
        return Promise.reject(error);
      } finally {
        isRefreshing = false;
      }
    }

    return Promise.reject(error);
  }
);

export default apiClient;
