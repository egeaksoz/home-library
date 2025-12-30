import "./Header.css";
import { useRef, type FC, useState } from "react";
import { Menu, X, House, Library } from "lucide-react";

const Header: FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const navRef = useRef<HTMLButtonElement>(null);

  const toggleSideMenu = (): void => {
    navRef.current!.classList.toggle("show");
    setIsOpen(!isOpen);
  };

  return (
    <header>
      <button onClick={toggleSideMenu}>{isOpen ? <X /> : <Menu />}</button>
      <nav ref={navRef}>
        <ul>
          <li>
            <a href="/">
              <House />
              <span>Home</span>
            </a>
          </li>
          <li>
            <a href="/libraries">
              <Library /> <span>Libraries</span>
            </a>
          </li>
        </ul>
      </nav>
      <div id="overlay" onClick={toggleSideMenu} aria-hidden="true"></div>
    </header>
  );
};

export default Header;
