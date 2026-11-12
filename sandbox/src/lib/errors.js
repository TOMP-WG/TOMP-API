class TompError extends Error {
  constructor({ errorcode = 9, type = 'OTHER', title, status = 400, detail, instance }) {
    super(title);
    this.errorcode = errorcode;
    this.type = type;
    this.title = title;
    this.status = status;
    this.detail = detail;
    this.instance = instance;
  }

  toBody() {
    return {
      errors: [
        {
          errorcode: this.errorcode,
          type: this.type,
          title: this.title,
          status: this.status,
          detail: this.detail,
          instance: this.instance,
        },
      ],
    };
  }
}

module.exports = { TompError };
