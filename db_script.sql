-- Таблица пользователей
CREATE TABLE users (
    id UUID PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    is_superuser BOOLEAN DEFAULT FALSE
);

-- Таблица компаний
CREATE TABLE companies (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);

-- Связующая таблица: пользователи и компании
CREATE TABLE user_company (
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    company_id UUID REFERENCES companies(id) ON DELETE CASCADE,
    role TEXT NOT NULL CHECK (role IN ('CREATOR', 'MEMBER')),
    PRIMARY KEY (user_id, company_id)
);

-- === Вставка пользователей ===
INSERT INTO users (id, username, email, is_superuser) VALUES
    ('3d18fc80-1c2b-4f7f-9d84-1a1a1d59e999', 'admin_user', 'admin@example.com', TRUE),
    ('7c293bba-a2f6-4f6e-8a0a-f0a5c0b90a11', 'john_doe', 'john@example.com', FALSE),
    ('95c8a19f-458c-45d7-b2b3-ff8b5e76c321', 'jane_smith', 'jane@example.com', FALSE);

-- === Вставка компаний ===
INSERT INTO companies (id, name, description) VALUES
    ('b3c3cb2a-2fc5-4c9d-91f7-6c5675d97a77', 'OpenAI Ltd', 'AI research and deployment company'),
    ('a9dcb2f3-4b45-4e3b-bcbe-3ac89791aabc', 'TechFlow Inc', 'Modern software development');

-- === Привязка пользователей к компаниям ===
INSERT INTO user_company (user_id, company_id, role) VALUES
    ('3d18fc80-1c2b-4f7f-9d84-1a1a1d59e999', 'b3c3cb2a-2fc5-4c9d-91f7-6c5675d97a77', 'ADMIN'),
    ('7c293bba-a2f6-4f6e-8a0a-f0a5c0b90a11', 'b3c3cb2a-2fc5-4c9d-91f7-6c5675d97a77', 'CREATOR'),
    ('7c293bba-a2f6-4f6e-8a0a-f0a5c0b90a11', 'a9dcb2f3-4b45-4e3b-bcbe-3ac89791aabc', 'MEMBER'),
    ('95c8a19f-458c-45d7-b2b3-ff8b5e76c321', 'a9dcb2f3-4b45-4e3b-bcbe-3ac89791aabc', 'CREATOR');
