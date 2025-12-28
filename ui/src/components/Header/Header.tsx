import "./Header.css";
import { type FC, useState } from "react";
import { X, Menu } from "lucide-react";

const Header: FC = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header>
      <button onClick={() => setIsOpen(!isOpen)}>
        {isOpen ? <X /> : <Menu />}
      </button>
      <nav>
        <ul className={isOpen ? "mobile-open" : "mobile-close"}>
          <li>
            <a href="/">
              <span>Home</span>
            </a>
          </li>
          <li>
            <a href="/libraries">Libraries</a>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
