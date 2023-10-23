#![allow(warnings)]
use std::collections::HashMap;

use pyo3::{prelude::*, py_run};
use pyo3::prelude::PyModule;
use pyo3::types::{PyTuple, PyList};

use pyo3::prelude::*;

fn main(){
    let asn_code = include_str!("/home/aki/projects/projectD/demon_nlp/src/nlp_classifier.py");
    // println!("{}",asn_code);

    Python::with_gil(|py|{
        let nlp_clf = PyModule::from_code(py, asn_code, "", "").unwrap();
        let args = PyTuple::new(py, &["models/math_classifier.joblib"]);
        nlp_clf.getattr("test_clf_model").unwrap().call1(args).unwrap();
    });
}





