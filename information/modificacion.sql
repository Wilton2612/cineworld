ALTER SCHEMA `cine`  DEFAULT CHARACTER SET utf8mb4  DEFAULT COLLATE utf8mb4_general_ci;

commit;

SELECT default_character_set_name FROM information_schema.SCHEMATA S WHERE schema_name = "cine";