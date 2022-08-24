rm reports.txt
rm built.txt

for recipe_name in */ ; do
    cd $recipe_name
    for d in */ ; do 
        firstletter=${recipe_name:0:1}
        if [[ $firstletter < 'g' ]]; then
            continue
        fi
        if [[ $firstletter > 'g' ]]; then
            continue
        fi
    
        cd $d
        version=$(cat conandata.yml | yq .sources | yq keys | yq .[0])
        full_recipe_name=$recipe_name$version@andrei/test
        echo "build $full_recipe_name"
        conan create . $full_recipe_name --build missing -ks
        retVal=$?
        echo "return code is $retVal for $full_recipe_name"
        if [ $retVal -eq 0 ]; then
          echo "$full_recipe_name" >> ../../built.txt
        fi
        cd ..
    done
    cd ..
done
