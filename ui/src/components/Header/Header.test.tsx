import { render, screen } from "@testing-library/react";
import Header from "./Header";
import { describe, it, expect } from "vitest";

describe("Header", () => {
  it("renders correctly", () => {
    render(<Header />);
    expect(screen.getByText("Welcome to your library!")).toBeInTheDocument();
  });
});
