import logo from "./logo.svg";
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { Route, Link, BrowserRouter, Routes } from "react-router-dom";
import Users from "./users";
import Contact from "./contact";
import Notfound from "./notfound";
import "bootstrap/dist/css/bootstrap.css";
import { Nav, Navbar, NavDropdown } from "react-bootstrap";

const routing = (
	<div>
		<BrowserRouter>
			<Navbar
				bg="dark"
				variant="dark"
				sticky="top"
				expand="sm"
				collapseOnSelect>
				<Navbar.Brand>
					<img src={logo} width="40px" height="40px" /> Logo
				</Navbar.Brand>

				<Navbar.Toggle className="coloring" />
				<Navbar.Collapse>
					<Nav>
						<NavDropdown title="Usuarios">
							<NavDropdown.Item href="/usuarios/1">Usuario 1</NavDropdown.Item>
							<NavDropdown.Item href="/usuarios/2">Usuario 2</NavDropdown.Item>
							<NavDropdown.Item href="/usuarios/3">Usuario 3</NavDropdown.Item>
							<NavDropdown.Divider />
							<NavDropdown.Item href="/usuarios">Todos</NavDropdown.Item>
						</NavDropdown>
						<Nav.Link href="/contacto">Contacto</Nav.Link>
						<Nav.Link href="/*">About Us</Nav.Link>
						<Nav.Link href="/*">Contact Us</Nav.Link>
					</Nav>
				</Navbar.Collapse>
			</Navbar>

			<Routes>
				<Route exact path="/" element={<App />} />
				<Route path="/usuarios/:id" element={<Users />} />
				<Route path="/contacto" element={<Contact />} />
				<Route path="*" element={<Notfound />} />
			</Routes>
		</BrowserRouter>
	</div>
);

ReactDOM.render(routing, document.getElementById("root"));
