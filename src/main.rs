#![allow(warnings)]
use pyo3::{prelude::*, py_run};
use pyo3::prelude::PyModule;
use pyo3::types::{PyTuple, PyList};

use pyo3::prelude::*;

fn main() -> PyResult<()> {
    let py_app = include_str!("/home/aki/projects/projectD/demon_nlp/src/test.py");
    let  from_python = Python::with_gil(|py| -> PyResult<Py<PyAny>> {
        let app: Py<PyAny> = PyModule::from_code(py, py_app, "", "")?
            .getattr("main")?
            .into();
        app.call0(py)
    });

    println!("py: {}", from_python?);
    Ok(())
}


