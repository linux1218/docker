use cho_db

CREATE TABLE `sample_tb`(
  `num`            BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `create_date`    DATETIME DEFAULT CURRENT_TIMESTAMP,
  `hostname`        VARCHAR(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE sample_tb ADD INDEX IDX_sample_tb_1(create_date ASC);
ALTER TABLE sample_tb ADD INDEX IDX_sample_tb_2(num ASC);