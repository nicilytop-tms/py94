create role prod_user nocreatedb createrole login;
alter user prod_user with password 'prod_user_password';
create database product_system owner prod_user encoding 'utf-8';