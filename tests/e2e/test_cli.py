def test_cli_outputs_report(tmp_path, capsys, cli_runner):
    """CLI should process CSV file and print formatted report."""

    file = tmp_path / "data.csv"
    file.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "video1,20.2,30,1000,100,3.5\n"  # included: ctr > 15 and retention_rate < 40
        "video2,11.4,50,2000,200,2.1\n"  # excluded: ctr < 15
        "video3,25,20,3000,300,4.0\n"  # included
    )

    cli_runner(["--files", str(file), "--report", "clickbait"])

    output = capsys.readouterr().out

    assert "video3" in output
    assert "video1" in output
    assert "video2" not in output


def test_cli_handles_data_error(tmp_path, capsys, cli_runner):
    """CLI should print error message when CSV is invalid."""

    file = tmp_path / "data.csv"
    file.write_text("ctr,retention_rate,views,likes,avg_watch_time\n20,30,1000,100,3.5\n")

    cli_runner(["--files", str(file)])

    output = capsys.readouterr().out

    assert "Data error" in output


def test_cli_handles_file_error(tmp_path, capsys, cli_runner):
    """CLI should print error message when file is missing."""

    file = tmp_path / "data.csv"

    cli_runner(["--files", str(file)])

    output = capsys.readouterr().out

    assert "File error" in output
