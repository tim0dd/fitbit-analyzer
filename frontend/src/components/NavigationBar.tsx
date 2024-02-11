// src/components/NavigationBar.tsx
import { useLocation, Link as RouterLink } from 'react-router-dom';
import { NavigationMenu, NavigationMenuList, NavigationMenuItem, NavigationMenuLink, navigationMenuTriggerStyle } from '@/components/ui/navigation-menu';
import { ThemeToggle } from '@/components/theme/ThemeToggle';
import { ReactNode } from 'react';
import '@/styles/nav.css';
interface NavLinkProps {
  to: string;
  children: ReactNode;
}

const NavLink: React.FC<NavLinkProps> = ({ to, children }) => {
  const location = useLocation();
  const isActive = location.pathname === to;

  return (
    <RouterLink to={to}>
      <NavigationMenuLink
        className={`${navigationMenuTriggerStyle()}`}
        active={isActive}
      >
        {children}
      </NavigationMenuLink>
    </RouterLink>
  );
};

const NavigationBar = () => {
  return (
    <NavigationMenu>
      <NavigationMenuList>
        <NavigationMenuItem>
          <NavLink to="/">Home</NavLink>
        </NavigationMenuItem>

        <NavigationMenuItem>
          <NavLink to="/dashboard">Dashboard</NavLink>
        </NavigationMenuItem>

        <NavigationMenuItem>
          <ThemeToggle />
        </NavigationMenuItem>
      </NavigationMenuList>
    </NavigationMenu>
  );
};

export default NavigationBar;