import "./Header.css";
import { type FC } from "react";

const Header: FC = () => {
  return (
    <header>
      <nav>
        <ul>
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
