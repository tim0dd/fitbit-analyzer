import { useNavigate } from "react-router-dom"; // For React Router v5
import { ThemeToggle } from "./theme/ThemeToggle";
import { Button } from "./ui/button";
import { Separator } from "./ui/separator";

type NavigationLinkProps = {
  to: string;
  children: React.ReactNode;
};

const NavigationLink: React.FC<NavigationLinkProps> = ({ to, children }) => {
  const navigate = useNavigate();

  const handleClick = (
    event: React.MouseEvent<HTMLAnchorElement, MouseEvent>
  ) => {
    event.preventDefault();
    navigate(to);
  };

  return (
    <a
      href={to}
      onClick={handleClick}
      // className="text-primary-foreground hover:text-seconday-foreground"
    >
      {children}
    </a>
  );
};

const NavigationBar = () => {
  // Assuming you have a way to determine if dark mode is active
  // const isDarkMode = useDarkMode();

  return (
    <div>
      <nav className="bg-background" style={{ color: "var(--foreground)" }}>
        <div className="max-w px-1">
          <div className="flex justify-between h-12 items-center">
            <div className="flex space-x-2">
              {/* Home Button */}
              <Button variant="outline" size="lg">
                <NavigationLink to="/">Home</NavigationLink>
              </Button>

              {/* Dashboard Button */}
              <Button variant="outline" size="lg">
                <NavigationLink to="/dashboard">Dashboard</NavigationLink>
              </Button>
            </div>
            <div className="flex items-center">
              <ThemeToggle />
            </div>
          </div>
        </div>
      </nav>
      <Separator />
    </div>
  );
};

export default NavigationBar;
