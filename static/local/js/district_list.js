let id_region = document.getElementById("region")

function set_district() {
    let distirct_url = "/regions/district/";
    let regionId = id_region.value;
    $.ajax({
        url: distirct_url,
        data: {
            'region': regionId
        },
        success: function (data) {
            $("#district").html(data);
        }
    });
}


// set_district();

id_region.addEventListener("change", function (e) {
    set_district();
})