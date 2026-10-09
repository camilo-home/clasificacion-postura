# -*- coding: utf-8 -*-
RANDOM_STATE = 42
MAX_FRAMES = 40

ejercicios = {
    1: "sentadilla",
    2: "peso muerto", 
    3: "curl biceps",
    4: "press banca"
}

vistas = {
    1: "frontal",
    2: "lateral"
}

CONFIG = {
    ("sentadilla", "lateral"): {"csv": "../data/raw/sentadilla_lateral.csv", "selected_ids": [12, 24, 26, 28], "mode": "angles"},
    ("sentadilla", "frontal"): {"csv": "../data/raw/sentadilla_frontal.csv", "selected_ids": [11,12,13,14,15,16,23,24,25,26], "mode": "symmetry"},
    ("peso muerto", "lateral"): {"csv": "../data/raw/peso_muerto_lateral.csv", "selected_ids": [12,14,16,24,26,28], "mode": "angles"},
    ("peso muerto", "frontal"): {"csv": "../data/raw/peso_muerto_frontal.csv", "selected_ids": [11,12,13,14,15,16,23,24,25,26], "mode": "symmetry"},
    ("curl biceps", "lateral"): {"csv": "../data/raw/curl_biceps_lateral.csv", "selected_ids": [12,14,16,24], "mode": "angles"},
    ("curl biceps", "frontal"): {"csv": "../data/raw/curl_biceps_frontal.csv", "selected_ids": [11,12,13,14,15,16], "mode": "symmetry"},
    ("press banca", "lateral"): {"csv": "../data/raw/press_banca_lateral.csv", "selected_ids": [12,14,16], "mode": "angles"},
    ("press banca", "frontal"): {"csv": "../data/raw/press_banca_frontal.csv", "selected_ids": [11,12,13,14,15,16], "mode": "symmetry"}
}

# NOMBRES FEATURES

FEATURE_NAMES = {

    ("sentadilla", "lateral"): [
        "angulo_rodilla",
        "angulo_cadera",
        "distancia_torso"
    ],

    ("sentadilla", "frontal"): [
        "simetria_hombros",
        "simetria_caderas",
        "simetria_rodillas",
        "dif_altura_hombros",
        "dif_altura_caderas",
        "dif_altura_rodillas",
        "inclinacion_hombros",
        "inclinacion_caderas",
        "diferencia_profundidad"
    ],

    ("peso muerto", "lateral"): [
        "angulo_rodilla",
        "angulo_cadera",
        "distancia_mano_rodilla"
    ],

    ("peso muerto", "frontal"): [
        "simetria_hombros",
        "simetria_caderas",
        "simetria_rodillas",
        "dif_altura_hombros",
        "dif_altura_caderas",
        "dif_altura_rodillas",
        "dif_altura_manos",
        "inclinacion_hombros",
        "inclinacion_caderas",
        "inclinacion_barra",
        "asimetria_brazos",
        "asimetria_piernas",
        "desplazamiento_lateral"
    ],

    ("curl biceps", "lateral"): [
        "angulo_codo",
        "distancia_codo_hombro",
        "distancia_codo_cadera",
        "distancia_muneca_hombro"
    ],

    ("curl biceps", "frontal"): [
        "simetria_hombros",
        "simetria_codos",
        "simetria_munecas",
        "dif_altura_munecas",
        "diferencia_angulos_codo"
    ],

    ("press banca", "lateral"): [
        "angulo_codo",
        "distancia_muneca_hombro"
    ],

    ("press banca", "frontal"): [
        "simetria_hombros",
        "simetria_codos",
        "simetria_munecas",
        "dif_altura_munecas",
        "diferencia_angulos_codo"
    ]
}