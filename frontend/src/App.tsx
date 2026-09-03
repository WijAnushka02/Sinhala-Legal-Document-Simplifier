import { useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { useAuthStore } from './store/authStore';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';

function App() {
  const { checkAuth, isLoading, isAuthenticated } = useAuthStore();

  useEffect(() => {
    // Silent auth check on page load
    checkAuth();
  }, [checkAuth]);

  if (isLoading) {
    return (
      <div className="loading-screen">
        <div className="spinner" />
        <p>නීතිමය ලේඛන සරල කිරීමේ පද්ධතිය…</p>
      </div>
    );
  }

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
