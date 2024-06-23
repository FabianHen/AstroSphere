function goBack() {
    window.location.href = window.location.href.split('/', window.location.href.split('/').length-1).join('/');
}