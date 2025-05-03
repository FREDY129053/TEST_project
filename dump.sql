--
-- PostgreSQL database dump
--

-- Dumped from database version 16.8
-- Dumped by pg_dump version 16.8

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: companies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.companies (
    id uuid NOT NULL,
    name text NOT NULL,
    description text
);


ALTER TABLE public.companies OWNER TO postgres;

--
-- Name: user_company; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_company (
    id integer NOT NULL,
    user_id uuid,
    company_id uuid,
    role text NOT NULL,
    CONSTRAINT user_company_role_check CHECK ((role = ANY (ARRAY['CREATOR'::text, 'MEMBER'::text])))
);


ALTER TABLE public.user_company OWNER TO postgres;

--
-- Name: user_company_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_company_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_company_id_seq OWNER TO postgres;

--
-- Name: user_company_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_company_id_seq OWNED BY public.user_company.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id uuid NOT NULL,
    username text NOT NULL,
    email text NOT NULL,
    is_superuser boolean DEFAULT false
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: user_company id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_company ALTER COLUMN id SET DEFAULT nextval('public.user_company_id_seq'::regclass);


--
-- Data for Name: companies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.companies (id, name, description) FROM stdin;
b3c3cb2a-2fc5-4c9d-91f7-6c5675d97a77	OpenAI Ltd	AI research and deployment company
a9dcb2f3-4b45-4e3b-bcbe-3ac89791aabc	TechFlow Inc	Modern software development
\.


--
-- Data for Name: user_company; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_company (id, user_id, company_id, role) FROM stdin;
1	7c293bba-a2f6-4f6e-8a0a-f0a5c0b90a11	b3c3cb2a-2fc5-4c9d-91f7-6c5675d97a77	CREATOR
2	7c293bba-a2f6-4f6e-8a0a-f0a5c0b90a11	a9dcb2f3-4b45-4e3b-bcbe-3ac89791aabc	MEMBER
3	95c8a19f-458c-45d7-b2b3-ff8b5e76c321	a9dcb2f3-4b45-4e3b-bcbe-3ac89791aabc	CREATOR
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, username, email, is_superuser) FROM stdin;
3d18fc80-1c2b-4f7f-9d84-1a1a1d59e999	admin_user	admin@example.com	t
7c293bba-a2f6-4f6e-8a0a-f0a5c0b90a11	john_doe	john@example.com	f
95c8a19f-458c-45d7-b2b3-ff8b5e76c321	jane_smith	jane@example.com	f
\.


--
-- Name: user_company_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_company_id_seq', 3, true);


--
-- Name: companies companies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_pkey PRIMARY KEY (id);


--
-- Name: user_company user_company_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_company
    ADD CONSTRAINT user_company_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: user_company user_company_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_company
    ADD CONSTRAINT user_company_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.companies(id) ON DELETE CASCADE;


--
-- Name: user_company user_company_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_company
    ADD CONSTRAINT user_company_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

