<?php

/* ******************************************************************************
# Nom ......... : traitement.php
# Rôle ........ : Traitement des données du formulaire et interaction avec la base de données.
# Auteur ...... : Maxim Khomenko
# Version ..... : V1.0.0 du 07/06/2024
# Licence ..... : Réalisé dans le cadre du cours de l'Informatique Fondamentale
# Usage ....... : Ce script doit être appelé par un formulaire HTML pour traiter et
#                 enregistrer les données saisies dans une base de données MySQL.
****************************************************************************** */

// Connexion à la base de données
$servername = "localhost";
$username = "root";
$password = "jcrTXr85yRJ_pe.";
$dbname = "formulaire";

// Afficher les erreurs
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Créer la connexion
$conn = new mysqli($servername, $username, $password, $dbname);

// Vérifier la connexion
if ($conn->connect_error) {
    die("La connexion a échoué: " . $conn->connect_error);
}

// Récupérer les données du formulaire avec la prévention des injections SQL
$nom = mysqli_real_escape_string($conn, $_POST['nom']);
$prenom = mysqli_real_escape_string($conn, $_POST['prenom']);
$email = mysqli_real_escape_string($conn, $_POST['email']);
$telephone = mysqli_real_escape_string($conn, $_POST['telephone']);
$date = mysqli_real_escape_string($conn, $_POST['date']);
$message = mysqli_real_escape_string($conn, $_POST['message']);
$notation = isset($_POST['notation']) ? intval($_POST['notation']) : null;

// Préparer la requête SQL avec une requête préparée pour l'insertion
$sql_insert = "INSERT INTO formulaire (nom, prenom, email, telephone, date, message, notation) VALUES (?, ?, ?, ?, ?, ?, ?)";
$stmt_insert = $conn->prepare($sql_insert);
$stmt_insert->bind_param("ssssssi", $nom, $prenom, $email, $telephone, $date, $message, $notation);

// Exécuter la requête d'insertion
if ($stmt_insert->execute()) {
    echo "Enregistrement réussi!";
} else {
    echo "Erreur lors de l'enregistrement: " . $stmt_insert->error;
}

// Fermer la requête d'insertion
$stmt_insert->close();

// Lire les données pour affichage (seulement la dernière personne)
$sql_select = "SELECT * FROM formulaire ORDER BY id DESC LIMIT 1";
$result = $conn->query($sql_select);

// Afficher les données
if ($result->num_rows > 0) {
    echo "<h2>Données enregistrées</h2>";
    $row = $result->fetch_assoc();
    echo "<p>Nom: " . $row["nom"] . "<br>Prenom: " . $row["prenom"] . "<br>Email: " . $row["email"] . "<br>Téléphone: " . $row["telephone"] . "<br>Date: " . $row["date"] . "<br>Message: " . $row["message"] . "<br>Notation: " . $row["notation"] . "</p>";
} else {
    echo "<p>Aucune donnée enregistrée.</p>";
}

// Fermer la connexion à la base de données
$conn->close();
?>