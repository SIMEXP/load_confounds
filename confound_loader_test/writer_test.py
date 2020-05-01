from load_confounds import load_confounds


with open("test_confounds_loader_reduced.py", "w") as test_writer:

    test_writer.write("from load_confounds import load_confounds \n")

    strategy = ["motion","minimal","high_pass_filter","matter","white_matter","compcor"]
    n_components = {"0.50","0.80","0.95"}
    motion_models = [
    "6params",
    "derivatives",
    "square", 
    "full"]

    for strat in strategy:

        if "," in strat:
            strat_in = strat.split(",")
            strat_in_str = str(strat_in)[1:-1]
        else:
            strat_in_str = '''"''' + strat + '''"'''
            strat_in = [strat]

        for motion in motion_models:

            if "," in motion:
                motion_in = motion.split(",")
                motion_in_str = str(motion_in)[1:-1]
            else:
                motion_in_str = '''"''' + motion + '''"'''
                motion_in = motion

            for comp in n_components:

                if "," in comp:
                    comp_in = comp.split(",")
                    comp_in_str = str(comp_in)[1:-1]
                else:
                    comp_in_str = str(comp )
                    comp_in = float(comp)


                confound_raw = "sub-01_ses-001.tsv"
                confound_raw = '''"''' +confound_raw+'''"'''


                function_name = "def test_confound_loader_%s_%s_%s(): \n" % (
                    strat.replace("-", "").replace(",", ""),
                    motion.replace("-", "").replace(",", ""),
                    comp.replace("0.","")

                )

                function_test = (
                    "load_confounds(confounds_raw = %s, strategy = [%s], motion_model = %s, n_components = %s).columns.values"
                    % (
                        confound_raw,
                        strat_in_str,
                        motion_in_str,
                        comp_in_str
                    )
                )

                function_out = str(
                    list(load_confounds(
                        "sub-01_ses-001.tsv",
                        strategy=strat_in,
                        motion_model=motion_in,
                        n_components=comp_in,
                    ).columns)
                )
                
                test_writer.write(function_name)
                test_writer.write("  assert ")

                test_writer.write("set("+function_test+")")
                test_writer.write(" == ")
                test_writer.write("set("+function_out+")")
                test_writer.write("\n")
                test_writer.write("\n\n")
