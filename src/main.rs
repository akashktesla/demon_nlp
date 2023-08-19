#![allow(warnings)]
use std::collections::HashMap;

use pyo3::{prelude::*, py_run};
use pyo3::prelude::PyModule;
use pyo3::types::{PyTuple, PyList};

use pyo3::prelude::*;

fn main(){
    let asn_code = include_str!("/home/aki/projects/projectD/demon_nlp/src/asn.py");

    Python::with_gil(|py|{

        let asn = PyModule::from_code(py, asn_code, "", "").unwrap();
        let args = PyTuple::new(py, &["I love apples"]);
        let a = asn.getattr("extract_dependency").unwrap().call1(args).unwrap();
        println!("out: {:?}",a);
        // let b:HashMap<String,Vec<String>> = a.extract().unwrap();

    });
}


