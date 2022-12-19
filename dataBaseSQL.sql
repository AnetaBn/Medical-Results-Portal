DROP DATABASE IF EXISTS pro_database;

CREATE DATABASE pro_database;

USE pro_database;

-- instrukcje do czyszczenia, jesli takie tabele istnieja
DROP TABLE IF EXISTS doctor;
DROP TABLE IF EXISTS study;
DROP TABLE IF EXISTS patient;

-- instrukcje do tworzenia odpowiednich tabel

CREATE TABLE patient
(
	-- klucz glowny
	patient_id SERIAL, 
	patient_name VARCHAR(50),
	age int,
	gender VARCHAR(4),
	PRIMARY KEY(patient_id)
);

CREATE TABLE doctor
(
	-- klucz glowny
	doctor_id SERIAL, 
	doctor_name VARCHAR(50),
	specialization VARCHAR(50),
	PRIMARY KEY (doctor_id)
);

CREATE TABLE study
(
	-- klucz glowny
	study_id SERIAL, 
	hospital VARCHAR(64),
	study_date DATE,
	modality VARCHAR(10),
    pathFile VARCHAR(100),
	-- klucz obcy
	patient_id BIGINT UNSIGNED,
	doctor_id BIGINT UNSIGNED,

    PRIMARY KEY(study_id),
	FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id)
);

-- for beginning, to remove later

INSERT INTO doctor (doctor_name, specialization) VALUES ('Anna May', 'radiology'); 
INSERT INTO doctor (doctor_name, specialization) VALUES ('John Watson', 'general medicine');
INSERT INTO patient (patient_name, age, gender) VALUES ('Sherlock Holmes', 40, 'male');
INSERT INTO study (hospital, study_date, modality, pathFile, patient_id, doctor_id) VALUES ('NN', '2000-01-01','CT','NN', (SELECT patient_id FROM patient WHERE patient_name ='Sherlock Holmes'), (SELECT doctor_id FROM doctor WHERE doctor_name ='Anna May'));