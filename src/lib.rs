#![allow(warnings)]
use pyo3::{prelude::*, py_run};
use pyo3::prelude::PyModule;
use pyo3::types::{PyTuple, PyList};
use pyo3::prelude::*;

pub fn predict(path:&String,text:&String)->Vec<String>{
    let asn_code = include_str!("/home/aki/projects/projectD/demon_nlp/src/nlp_classifier.py");

    let mut returns = Vec::new();
    Python::with_gil(|py|{
        let nlp_clf = PyModule::from_code(py, asn_code, "", "").unwrap();
        let args = PyTuple::new(py, &[path,text]);
        let r = nlp_clf.getattr("predict_clf").unwrap().call1(args).unwrap();
        returns = r.extract().unwrap();
        // println!("{:?}",returns);
    });
    return returns;
}
