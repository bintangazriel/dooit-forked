$("#id_jenis").change(function () {
    var url = $("#catatanTransaksiForm").attr("data-kategoris-url");
    var jenisId = $(this).val();

    $.ajax({
      url: url,
      data: {
        'jenis': jenisId
      },
      success: function (data) {
        $("#id_kategori").html(data);
      }
    });

  });