    (* Écrivez la fonction nbPosit qui calcule le nombre d'entiers strictement positifs d'une liste d'entiers.
    Exemples :
        (nbPosit [2;-3;1;-1]) vaut 2
        (nbPosit [-2;-3;-1;-1]) vaut 0
        (nbPosit [2;3;1;1]) vaut 4

    Écrivez la fonction tousPosit qui vérifie si tous les éléments d'une liste d'entiers sont strictement positifs.
    Exemples :
        (tousPosit [2;-3;1;-1]) vaut false
        (tousPosit []) vaut true
        (tousPosit [2;3;1;1]) vaut true

    Écrivez la fonction liPosit qui extrait la liste des entiers strictement positifs d'une liste d'entiers.
    Exemples :
        (liPosit [2;-3;1;-1]) vaut [2;1]
        (liPosit []) vaut []
        (liPosit [2;3;1;1]) vaut [2;3;1;1]

    Écrivez la fonction oterPosit qui supprime d'une liste d'entiers tous les éléments strictement positifs.
    Exemples :
        (oterPosit [2;-3;1;-1]) vaut [-3;-1]
        (oterPosit []) vaut []
        (oterPosit [2;3;1;1]) vaut [] *)

let rec nbPosit  = function
  |[] -> 0
  |e::l when e > 0 -> 1 + nbPosit(l)
  |e::l -> nbPosit(l)
;;

let rec tousPosit = function
  |[] -> true
  |e::l when e > 0 -> tousPosit(l)
  |e::l -> false
;;

let rec liPosit =
  "à remplacer"
;;

let rec oterPosit =
  "à remplacer"
;;

print_int (nbPosit [2;-3;1;-1]);; (*vaut 2*)
print_newline ();;
print_int (nbPosit [-2;-3;-1;-1]);; (*vaut 0*)
print_newline ();;
print_int (nbPosit [2;3;1;1]);; (*vaut 4*)
print_newline ();;
print_string (string_of_bool  (tousPosit [2;-3;1;-1]));; (*vaut false*)
print_newline ();;
print_string (string_of_bool  (tousPosit []));; (*vaut true*)
print_newline ();;
print_string (string_of_bool  (tousPosit [2;3;1;1]));; (*vaut true*)
print_newline ();;
(liPosit [2;-3;1;-1]) (* vaut) [2;1]*)
print_newline ();;
(liPosit []) (* vaut) []*)
print_newline ();;
(liPosit [2;3;1;1]) (* vaut) [2;3;1;1]*)
print_newline ();;
(*(oterPosit [2;-3;1;-1]) vaut [-3;-1]
(oterPosit []) vaut []
(oterPosit [2;3;1;1]) vaut [] *)