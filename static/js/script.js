function addFormacao() {
  document.getElementById("formacoes").insertAdjacentHTML("beforeend",
    '<input type="text" name="curso" placeholder="Curso"> ' +
    '<input type="text" name="instituicao" placeholder="Instituição"><br>');
}

function addExperiencia() {
  document.getElementById("experiencias").insertAdjacentHTML("beforeend",
    '<input type="text" name="empresa" placeholder="Empresa"> ' +
    '<input type="text" name="cargo" placeholder="Cargo"><br>');
}
