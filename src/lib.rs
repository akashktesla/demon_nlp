#![allow(warnings)]
use pyo3::{prelude::*, py_run};
use pyo3::prelude::PyModule;
use pyo3::types::{PyTuple, PyList};
use pyo3::prelude::*;

pub fn predict(path:&String,text:&String){
    let asn_code = include_str!("/home/aki/projects/projectD/demon_nlp/src/nlp_classifier.py");

    Python::with_gil(|py|{

        let nlp_clf = PyModule::from_code(py, asn_code, "", "").unwrap();
        let args = PyTuple::new(py, &[path,text]);
        nlp_clf.getattr("predict_clf").unwrap().call1(args).unwrap();
    });

}
