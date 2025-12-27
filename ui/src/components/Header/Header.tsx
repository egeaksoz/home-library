import "./Header.css";
import { type FC } from "react";

const Header: FC = () => {
  return (
    <header>
      <nav>
        <ul>
          <li>Home</li>
          <li>Libraries</li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
