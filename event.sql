CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    role ENUM('Admin', 'Organizer', 'Attendee'),
    password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    organizer_id INT,
    title VARCHAR(150),
    description TEXT,
    date DATETIME,
    venue VARCHAR(255),
    status ENUM('Pending', 'Approved', 'Rejected'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (organizer_id) REFERENCES Users(id)
);

CREATE TABLE Tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    price DECIMAL(10, 2),
    quantity INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES Events(id)
);

CREATE TABLE Registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    attendee_id INT,
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES Events(id),
    FOREIGN KEY (attendee_id) REFERENCES Users(id)
);

CREATE TABLE Messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    sender_id INT,
    message TEXT,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES Events(id),
    FOREIGN KEY (sender_id) REFERENCES Users(id)
);
