import React, { Component } from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			articulos: [
				{
					codigo: 1,
					descripcion: "coca cola",
					precio: 2.5,
				},
				{
					codigo: 2,
					descripcion: "inka cola",
					precio: 2.2,
				},
				{
					codigo: 3,
					descripcion: "fanta",
					precio: 1.7,
				},
			],
		};
	}
	render() {
		return (
			<div>
				<table border="1" class="table table-dark">
					<thead>
						<tr>
							<th>Codigo</th>
							<th>Descripcion</th>
							<th>Precio</th>
							<th>Borrar</th>
						</tr>
					</thead>
					<tbody>
						{this.state.articulos.map((elemento) => {
							return (
								<tr key={elemento.codigo}>
									<td>{elemento.codigo}</td>
									<td>{elemento.descripcion}</td>
									<td>{elemento.precio}</td>
									<td>
										<button onClick={() => this.borrar(elemento.codigo)}>
											Borrar
										</button>
									</td>
								</tr>
							);
						})}
					</tbody>
				</table>
			</div>
		);
	}
	borrar(cod) {
		var temp = this.state.articulos.filter((el) => el.codigo !== cod);
		this.setState({ articulos: temp });
	}
}
export default App;
