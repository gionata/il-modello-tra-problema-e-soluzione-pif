<template>
    <div text-center>
        <div class="qr">
            <img src="/assets/qr.svg" alt="QR" />
        </div>
    </div>
</template>

<style lang="css" scoped>
.qr {
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    display: inline-block;
    height: 7em;
    width: 7em;
    transform: translateY(-12mm) !important;
}
@media print {
    .qr {
        /* sposta il codice QR verso l'alto di 2 cm nella stampa */
        transform: translateY(-48mm) !important;
    }
}
</style>
