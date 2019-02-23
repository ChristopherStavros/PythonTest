DROP TABLE IF EXISTS public.users;

CREATE TABLE public.users(
    id SERIAL PRIMARY KEY,
    email character VARYING(255),
    first_name character VARYING(255),
    last_name character VARYING(255),
    oauth_token character VARYING(255),
    oauth_token_secret character VARYING(255)
);