for recipe_name in */ ; do
    cd $recipe_name
    for d in */ ; do 
        firstletter=${recipe_name:0:1}
        if [[ $firstletter < 'd' ]]; then
            continue
        fi
        if [[ $firstletter > 'f' ]]; then
            continue
        fi
    
        cd $d
        version=$(cat conandata.yml | yq .sources | yq keys | yq .[0])
        full_recipe_name=$recipe_name$version@andrei/test
        echo "build $full_recipe_name"
        conan create . $full_recipe_name --build missing -ks > local_build.txt
        cat local_build.txt
        echo "return code is $?"
        cd ..
    done
    cd ..
done
