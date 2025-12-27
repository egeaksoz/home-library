import { render } from "@testing-library/react";
import Header from "./Header";
import { describe, it, expect } from "vitest";

describe("Header", () => {
  it("renders correctly", () => {
    const { container } = render(<Header />);
    expect(container.querySelector("header")).toBeInTheDocument();
  });

  it("renders navigation", () => {
    const { container } = render(<Header />);
    expect(container.querySelector("nav")).toBeInTheDocument();
    expect(container.querySelector("ul")).toBeInTheDocument();
    expect(container.querySelector("li")).toBeInTheDocument();
    expect(container.querySelector("li")).toBeInTheDocument();
  });

  it("select navbar items", () => {
    const { getByText } = render(<Header />);
    expect(getByText("Home")).toBeInTheDocument();
    expect(getByText("Libraries")).toBeInTheDocument();
  });
});
