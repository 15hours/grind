package main
// 11. Деревья. На вход бинарное дерево, элементы которого заглавные латинские
//     буквы. Нужно понять, существуют ли два эквивалентных узла. Узлы
//     эквивалетны, если поддерево от одного узла равно поддереву второго.
//     Равенство определяется наличием одинаковых символов на вершинах. Частоты не
//     важны.Пример:
//          F
//       /     \
//     !D       !H
//   /    \     / \ 
// H       G   D   G
//                  \
//                   D
// Здесь ответ: вершины, с воскл знаками. То есть поддерево от D равно поддереву от H. Две D в вправом поддерреве - тоже ответ

traverse(node) (map[byte]bool, bool) {
    if node == nil {
        return map[byte]bool{}, false
    }

    m := map[byte]bool

    mLeft, isEqual1 := traverse(node.Left)
    mRight, isEqual2 := traverse(node.Right)

    if isEqual1 || isEqual2 || deepEqual(mLeft, mRight) {
        return map[byte]bool{}, true
    }

    for k, _ := mLeft {
        m[k] = true
    }

    for k, _ := mRgith {
        m[k] = true
    }

    return m, false
}

func main() {
    _, result := traverse(root)
    return result
}
