<?php
    $lecture_id = $_GET["lecture"];
    $program_dir = escapeshellarg("../../server/statistics.py");
    echo exec("../../../python_env/bin/python3 $program_dir $lecture_id");
    echo "OK";

