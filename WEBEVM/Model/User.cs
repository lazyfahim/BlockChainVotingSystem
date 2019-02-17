using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNet.Identity.EntityFramework;

namespace Model
{
    public class User:IdentityUser
    {
        public User()
            : this(string.Empty, string.Empty)
        {
        }

        public User(string userName, string email)
            : base(userName)
        {
            this.Email = email;
            this.UserName = userName;
            //this.CreatedOn = DateTime.Now;
        }
        public override string UserName { get; set; }
        public override string Email { get; set; }
        [ForeignKey("ProfilePic")]
        public Guid? ImageId { get; set; }
        public virtual Image ProfilePic { get; set; }
    }
}
