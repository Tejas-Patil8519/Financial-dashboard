-- MySQL 8+ example query. Rename table/columns if needed.
SELECT month, revenue, expenses, revenue-expenses AS profit, expenses-budget AS budget_variance FROM finance ORDER BY month;
