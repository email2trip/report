$pdf_mode = 1;
$pdflatex = 'pdflatex -interaction=nonstopmode -file-line-error %O %S';
$max_repeat = 5;

my $chktex_ran = 0;

sub run_chktex_once {
    return 0 if $chktex_ran;
    $chktex_ran = 1;

    my $cmd = q{sh -c 'if ! command -v chktex >/dev/null 2>&1; then exit 0; fi; find . -type f -name "*.tex" -print0 | xargs -0 chktex -q -I0'};
    my $status = system($cmd);

    if ($status != 0) {
        print "\n=== ChkTeX warnings detected ===\n";
        print "Review the messages above. PDF compilation will continue.\n\n";
    }

    return 0;
}

add_hook( 'before_xlatex', 'run_chktex_once' );
