cd recipes/
sucessfull_builds=$(grep -R "(test package): Running test()" | cut -d "/" -f1)
echo $sucessfull_builds
for recipe_name in ${sucessfull_builds} ; do
    firstletter=${recipe_name:0:1}
    if [[ $firstletter < 'c' ]]; then
        continue
    fi
    if [[ $firstletter > 'f' ]]; then
        continue
    fi

    echo $recipe_name
    cd ${recipe_name}/
    branch_name="migrate_${recipe_name}_to_conan_v2_try5"
    echo $branch_name
    git br $branch_name
    git co $branch_name
    git add -u  .
    git commit -m "migrate $recipe_name to conan v2"
    git push my HEAD
    cd ..
    git co master
done
