git reset master
cd recipes/
sucessfull_builds=$(cat built.txt)
echo $sucessfull_builds
for full_recipe_name in ${sucessfull_builds} ; do
    echo "full_recipe_name is $full_recipe_name"

    firstletter=${recipe_name:0:1}
    #if [[ $firstletter < 'g' ]]; then
    #    continue
    #fi
    #if [[ $firstletter > 'g' ]]; then
    #    continue
    #fi
    
    recipe_name=$(echo $full_recipe_name | cut -d "/" -f1)
    echo $recipe_name
    cd ${recipe_name}/
    branch_name="migrate_${recipe_name}_to_conan_v2_try7"
    echo $branch_name
    git br $branch_name
    git co $branch_name
    git add -u  .
    git commit -m "migrate $recipe_name to conan v2"
    git push my HEAD
    cd ..
    git co master
    sleep 3
done
