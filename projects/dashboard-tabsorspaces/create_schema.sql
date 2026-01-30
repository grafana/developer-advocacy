-- Database schema for tabs-or-spaces analysis results
-- Database: tabs-or-spaces
-- Cloud SQL Instance: ronald-dashboard-data-gen

USE `tabs-or-spaces`;

-- Main table to store analysis results
CREATE TABLE IF NOT EXISTS `analysis_results` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `test_date` DATE NOT NULL,
    `repo_owner` VARCHAR(255) NOT NULL,
    `repo_name` VARCHAR(255) NOT NULL,
    `indentation_type` ENUM('Tabs', 'Spaces', 'Mixed (tabs and spaces)', 'None detected') NOT NULL,
    `files_processed` INT UNSIGNED NOT NULL DEFAULT 0,
    `lines_processed` INT UNSIGNED NOT NULL DEFAULT 0,
    `deepest_indentation_level` INT UNSIGNED NOT NULL DEFAULT 0,
    `average_indentation_level` DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    `files_tabs_only` INT UNSIGNED NOT NULL DEFAULT 0,
    `files_spaces_only` INT UNSIGNED NOT NULL DEFAULT 0,
    `files_mixed` INT UNSIGNED NOT NULL DEFAULT 0,
    `avg_spaces_per_indent` DECIMAL(10, 2) NULL DEFAULT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `unique_test_repo` (`test_date`, `repo_owner`, `repo_name`),
    KEY `idx_test_date` (`test_date`),
    KEY `idx_repo_owner` (`repo_owner`),
    KEY `idx_repo_name` (`repo_name`),
    KEY `idx_owner_repo` (`repo_owner`, `repo_name`),
    KEY `idx_date_owner` (`test_date`, `repo_owner`),
    KEY `idx_indentation_type` (`indentation_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Additional composite index for queries filtering by indentation type and date
-- (e.g., "show me all repos using tabs on a specific date range")
CREATE INDEX `idx_type_date` ON `analysis_results` (`indentation_type`, `test_date`);

