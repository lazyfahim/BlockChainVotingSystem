using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Web;

namespace Model
{
    public class Image:Entity
    {
        public string Title { get; set; }
        [NotMapped]
        public HttpPostedFileBase File { get; set; }
        public string ImagePath { get; set; }
    }
}
