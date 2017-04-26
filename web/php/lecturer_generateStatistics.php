<?php
    $lecture_id = $_GET["lecture_id"];
    $program_dir = escapeshellarg("../../pugruppe100/server/statistics.py");
    echo exec("../../python_env/bin/python3 $program_dir $lecture_id");
    echo "OK";

