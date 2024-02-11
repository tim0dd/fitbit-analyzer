import { ThemeProvider } from "@/components/theme/ThemeProvider"
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import NavigationBar from './components/NavigationBar';
import DashboardPage from './pages/DashboardPage';

function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
    <Router>
      <NavigationBar /> {/* This replaces the previous nav element */}

      <Routes>
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/" element={<Home />} />
        {/* Other routes go here */}
      </Routes>
    </Router>
    </ThemeProvider>
  );
}

export default App;

// Home component (can be in a separate file)
function Home() {
  return <h2>Home Page</h2>;
}
